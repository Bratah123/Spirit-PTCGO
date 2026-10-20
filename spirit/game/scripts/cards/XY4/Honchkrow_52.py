from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if


def _defender_asleep(ctx):
    d = ctx.defender
    return d is not None and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] in (
        d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="ed539843-200f-5a4e-a0b2-a06a9f816520",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Nightmare Mambo",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 60 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_defender_asleep, 60),
        ),
    ],
)