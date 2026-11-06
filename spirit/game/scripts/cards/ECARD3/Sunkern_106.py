from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="e3417533-fea8-5b4f-bad2-8c0e171effd5",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic", "Sunkern"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=191,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Blot",
            game_text="If there are any damage counters on Sunkern, remove 1 of them.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)
