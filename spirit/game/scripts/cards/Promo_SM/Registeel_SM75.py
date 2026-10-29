from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.sm4 import iron_hand


card = PokemonCardDef(
    guid="f964da9f-b9cc-5e45-b4c0-d50217fd8093",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic", "Registeel"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Attack(
            title="Turbo Arm",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target=lambda p: not is_in_active_spot(p), prompt='Choose a basic Energy card to attach to a Benched Pokémon'),
        ),
        Attack(
            title="Iron Fist",
            game_text="If Regice is on your Bench, heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=iron_hand,
        ),
    ],
)