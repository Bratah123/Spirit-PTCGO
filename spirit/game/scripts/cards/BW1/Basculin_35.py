from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca03358b-789d-5506-b73f-0619a0304841",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic", "Basculin"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)