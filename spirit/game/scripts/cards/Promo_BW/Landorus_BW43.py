from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="cf73100e-6bda-561e-8ad1-e2844423c890",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic", "Landorus"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=645,
    abilities=[
        Attack(
            title="Abundant Harvest",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1, target="self",
                prompt="Choose a basic Energy card to attach.",
            ),
        ),
        Attack(
            title="Gaia Hammer",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=spread_damage(10, side="both", also_base=True),
        ),
    ],
)
