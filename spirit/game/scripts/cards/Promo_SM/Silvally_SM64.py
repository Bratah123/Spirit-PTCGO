from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="abea2da9-069b-57ee-9f51-87dee3f78ad2",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silvally.Name",
    display_name="Silvally",
    searchable_by=["Silvally", "Stage 1", "Silvally"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=773,
    abilities=[
        Attack(
            title="Gear Scan",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_item_card, count=1, minimum=0, reveal=True),
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)