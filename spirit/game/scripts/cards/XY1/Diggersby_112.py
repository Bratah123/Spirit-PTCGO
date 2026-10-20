from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="ae10087a-1fd3-5ab0-b61e-3ba0de6fc7c8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name",
    display_name="Diggersby",
    searchable_by=["Diggersby", "Stage 1", "Diggersby"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    family_id=659,
    abilities=[
        Attack(
            title="Pickup",
            game_text="Put 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=recover_from_discard(is_item_card, count=2, minimum=1, prompt='Choose 2 Item cards to put into your hand'),
        ),
        Attack(
            title="Dig",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)