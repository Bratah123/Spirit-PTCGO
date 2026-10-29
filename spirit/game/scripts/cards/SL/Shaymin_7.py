"""STUB: effect not implemented — do not guess mechanics.
Shaymin (SL #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


card = PokemonCardDef(
    guid="d57e19a0-ef06-59ae-a53e-6db4ffdb62a0",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Flippity Flap",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Rally Back",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.kos_suffered_last_turn() > 0, 90),
        ),
    ],
)