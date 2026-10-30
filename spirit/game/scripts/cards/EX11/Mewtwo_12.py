"""STUB: effect not implemented — do not guess mechanics.
Mewtwo δ (EX11 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.card_effects.ex import delta_switch_on_play, energy_burst_both_sides
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8e42d5e0-a11e-5f2b-bc2d-19102ddc9d30",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo δ",
    searchable_by=["Mewtwo \u03b4", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Delta Switch",
            game_text="Once during your turn, when you put Mewtwo from your hand onto your Bench, you may move any number of basic Energy cards attached to your Pok\u00e9mon to your other Pok\u00e9mon (excluding Mewtwo) in any way you like.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=delta_switch_on_play(),
        ),
        Attack(
            title="Energy Burst",
            game_text="Does 10 damage times the total amount of Energy attached to Mewtwo and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            effect=energy_burst_both_sides(10),
        ),
    ],
)