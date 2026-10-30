from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_for_bonus
from spirit.game.card_effects.ex import rough_skin
from spirit.game.card_effects.pokemon import energy_provides_type


def _is_darkness_energy(card):
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)


card = PokemonCardDef(
    guid="c713de78-d71a-5718-8850-543fb3483b56",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If Sharpedo is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Sharpedo is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=rough_skin(2),
        ),
        Attack(
            title="Dark Slash",
            game_text="You may discard a Darkness Energy card attached to Sharpedo. If you do, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=discard_for_bonus(
                source="self-energy", predicate=_is_darkness_energy, flat=30,
                prompt="You may discard a Darkness Energy card",
            ),
        ),
    ],
)
