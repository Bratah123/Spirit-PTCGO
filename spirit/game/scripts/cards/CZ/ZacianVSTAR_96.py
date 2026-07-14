from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="affcb5be-2ebd-587a-9d04-76a65a38e2a2",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVSTAR.Name",
    display_name="Zacian VSTAR",
    searchable_by=["Zacian VSTAR", "VSTAR", "ZacianVSTAR"],
    subtypes=["VSTAR"],
    collector_number=96,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    family_id=888,
    abilities=[
        Attack(
            title="Break Edge",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
        Attack(
            title="Sword Star",
            game_text="This Pok\u00e9mon also does 30 damage to itself. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=310,
            effect=unimplemented,
        ),
    ],
)