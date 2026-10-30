from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14b177c0-92ea-5122-941e-3f953db0b3c3",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    display_name="Team Aqua's Carvanha",
    searchable_by=["Team Aqua's Carvanha", "Basic", "TeamAquasCarvanha"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)