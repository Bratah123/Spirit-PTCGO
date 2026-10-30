"""STUB: effect not implemented — do not guess mechanics.
Tyranitar ex (EX10 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.ex import discard_special_energy_from_defender, discard_stadium_then_damage, mill_opponent_top


card = PokemonCardDef(
    guid="88abb085-b6e1-5658-ba48-99a93a178490",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex",
    searchable_by=["Tyranitar ex", "Stage 2", "ex", "Tyranitarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=111,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Shatter",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=discard_stadium_then_damage(),
        ),
        Attack(
            title="Derail",
            game_text="Discard a Special Energy card, if any, attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=discard_special_energy_from_defender(),
        ),
        Attack(
            title="Mix-Up",
            game_text="Your opponent discards the top card of his or her deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=mill_opponent_top(1),
        ),
        Attack(
            title="Losing Control",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=mill_attack(3, opponent=False),
        ),
    ],
)