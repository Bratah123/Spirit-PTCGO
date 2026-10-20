from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import mill_attack, discard_for_bonus


def _is_item(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.ITEM.value, TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


card = PokemonCardDef(
    guid="ed483bf4-fdaf-5cc9-bbbd-d443286aec69",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1", "Pangoro"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=674,
    abilities=[
        Attack(
            title="Clobber",
            game_text="You may discard an Item card from your hand. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=discard_for_bonus(source='hand', predicate=_is_item, flat=40,
                prompt='You may discard an Item card for 40 more damage'),
        ),
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=mill_attack(1),
        ),
    ],
)