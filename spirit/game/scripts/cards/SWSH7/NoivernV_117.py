from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_all_opponents


def _same_hand_size(ctx) -> bool:
    return ctx.hand_size(ctx.player_id) == ctx.hand_size(ctx.opponent_id)


card = PokemonCardDef(
    guid="f9499785-b8b2-5571-ac3b-56b019a23377",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernV.Name",
    display_name="Noivern V",
    searchable_by=["Noivern V", "Basic", "V", "NoivernV"],
    subtypes=["Basic", "V"],
    collector_number=117,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=715,
    abilities=[
        Attack(
            title="Boomburst",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=damage_all_opponents(20),
        ),
        Attack(
            title="Synchro Loud",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 120),
        ),
    ],
)