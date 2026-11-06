from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="64de7e6f-678a-5f3c-ad23-5cb0012dbdb2",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=231,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage times the number of damage counters on Phanpy.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
