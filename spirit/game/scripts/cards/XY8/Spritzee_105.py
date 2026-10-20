from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


card = PokemonCardDef(
    guid="4405fdab-73f5-55d6-8b1e-208644b7c78f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    display_name="Spritzee",
    searchable_by=["Spritzee", "Basic", "Spritzee"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=682,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 10),
        ),
    ],
)