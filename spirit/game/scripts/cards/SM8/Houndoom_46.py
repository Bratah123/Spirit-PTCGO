from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import bonus_if

_more_cards_in_hand = lambda ctx: ctx.hand_size(ctx.player_id) > ctx.hand_size(ctx.opponent_id)

card = PokemonCardDef(
    guid="b04c4336-9374-57f0-94d1-7a14cd706cd3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(count=1, minimum=0, reveal=False),
        ),
        Attack(
            title="Attack Operation",
            game_text="If you have more cards in your hand than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_more_cards_in_hand, 80),
        ),
    ],
)