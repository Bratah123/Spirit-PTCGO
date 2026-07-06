from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92236790-2c73-56ed-b409-acf2bb56e82e",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlakingV.Name",
    display_name="Slaking V",
    searchable_by=["Slaking V", "Basic", "V", "SlakingV"],
    subtypes=["Basic", "V"],
    collector_number=58,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=289,
    abilities=[
        Ability(
            title="Kinda Lazy",
            game_text="If you have exactly 2, 4, or 6 Prize cards remaining, this Pok\u00e9mon can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.COLORLESS: 4},
            damage=260,
        ),
    ],
)