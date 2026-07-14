from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9d18688-fd81-5039-a1a3-5b897cbc9bad",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraVSTAR.Name",
    display_name="Zeraora VSTAR",
    searchable_by=["Zeraora VSTAR", "VSTAR", "ZeraoraVSTAR"],
    subtypes=["VSTAR"],
    collector_number=55,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    family_id=807,
    abilities=[
        Attack(
            title="Crushing Beat",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Storm Star",
            game_text="Choose 1 of your opponent's Pok\u00e9mon 4 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 60 damage to it. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)