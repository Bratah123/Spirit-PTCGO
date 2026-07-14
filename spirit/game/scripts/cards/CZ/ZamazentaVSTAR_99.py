from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad9a6f18-d2fa-5436-a862-93ac3087a39b",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaVSTAR.Name",
    display_name="Zamazenta VSTAR",
    searchable_by=["Zamazenta VSTAR", "VSTAR", "ZamazentaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=99,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    family_id=889,
    abilities=[
        Ability(
            title="Shield Star",
            game_text="During your turn, you may use this Ability. During your opponent's next turn, all of your Pok\u00e9mon take 100 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). (This includes Pok\u00e9mon that come into play during this turn or during your opponent's next turn.) (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)