    ######################################################################
    # READ AN ACCOUNT
    ######################################################################
    @app.route("/accounts/<int:account_id>", methods=["GET"])
    def get_accounts(account_id):
        """
        Reads an Account
        This endpoint will read an Account based the account_id that is requested
        """
        app.logger.info("Request to read an Account with id: %s", account_id)

        account = Account.find(account_id)
        if not account:
            abort(status.HTTP_404_NOT_FOUND, f"Account with id [{account_id}] could not be found.")

        return account.serialize(), status.HTTP_200_OK
