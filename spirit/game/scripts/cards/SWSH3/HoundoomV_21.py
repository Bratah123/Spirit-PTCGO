from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import bonus_if, condition_attack


def _benched_fire_has_damage(ctx):
    for pokemon in ctx.my_bench():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.FIRE.value in types and \
                pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            return True
    return False


card = PokemonCardDef(
    guid="b5390f15-4b6f-521f-8da2-e26b96f23813",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomV.Name",
    display_name="Houndoom V",
    searchable_by=["Houndoom V", "Basic", "V", "HoundoomV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=229,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Vengeful Flame",
            game_text="If your Benched Fire Pokémon have any damage counters on them, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_benched_fire_has_damage, 100),
        ),
    ],
)
