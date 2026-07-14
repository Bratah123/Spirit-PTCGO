from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack, recover_from_discard, requires_discard
from spirit.game.session.effects import is_item_card

hold_still = heal_attack(30, target="self")

ideal_fishing_day = recover_from_discard(
    predicate=is_item_card, count=1, minimum=1, reveal=False, to="hand",
    prompt="Choose an Item card to put into your hand.",
)

card = PokemonCardDef(
    guid="e0fda57c-5575-5f1b-8484-6d4c3260ec86",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hold_still,
        ),
        Attack(
            title="Ideal Fishing Day",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.WATER: 1},
            effect=ideal_fishing_day,
            condition=requires_discard(is_item_card),
        ),
    ],
)