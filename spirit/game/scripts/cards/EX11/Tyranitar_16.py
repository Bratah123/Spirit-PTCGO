"""STUB: effect not implemented — do not guess mechanics.
Tyranitar δ (EX11 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import crush_draw_any, delta_crush_optional, poke_power_condition
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a3e91ad8-e151-5235-8c74-ea10cdc5fa20",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar δ",
    searchable_by=["Tyranitar \u03b4", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=248,
    abilities=[
        Ability(
            title="Crush Draw",
            game_text="Once during your turn (before your attack), you may reveal the top card of your deck. If that card is a basic Energy card, attach it to 1 of your Pok\u00e9mon. If not, put the card back on top of your deck. This power can't be used if Tyranitar is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=crush_draw_any(),
        ),
        Attack(
            title="Delta Crush",
            game_text="You may discard an Energy card attached to Tyranitar. If you do, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=delta_crush_optional(50, 20),
        ),
    ],
)