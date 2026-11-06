from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack, discard_for_bonus
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="ab9cf221-8501-5095-88bd-9c6f82627fd1",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Sand-Attack",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Fire Slash",
            game_text="You may discard a Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=discard_for_bonus(source='self-energy', predicate=_is_fire_energy, max_count=1, flat=30,
                                     prompt='You may discard a Fire Energy for 30 more damage'),
        ),
    ],
)