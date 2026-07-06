from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1db5591-eb82-5402-9d57-8502335e1a69",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1", "Frosmoth"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH45",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Ability(
            title="Ice Dance",
            game_text="As often as you like during your turn, you may attach a Water Energy card from your hand to 1 of your Benched Water Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)