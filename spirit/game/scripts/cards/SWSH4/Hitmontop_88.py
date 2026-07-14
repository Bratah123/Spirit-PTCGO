from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import discard_then_draw
from spirit.game.card_effects.attacks_common import bonus_if


def _played_bea(ctx):
    return ctx.played_trainer_this_turn("Bea") > 0


card = PokemonCardDef(
    guid="f6517430-0c8a-5700-831b-68aa8b3020b8",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title="Cycle Draw",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_then_draw(1, 3),
        ),
        Attack(
            title="Tornado Kick",
            game_text="If you played Bea from your hand during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_played_bea, 80),
        ),
    ],
)