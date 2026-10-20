from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play
from spirit.game.content.definitions import def_for


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


card = PokemonCardDef(
    guid="b61e5319-75ce-54fc-bb5d-0100e636ad0d",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic", "Pawniard"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=624,
    abilities=[
        Attack(
            title="Charge Order",
            game_text="This attack does 10 damage times the number of your Pawniard.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", lambda p: _named(p, "Pawniard")), 10),
        ),
    ],
)