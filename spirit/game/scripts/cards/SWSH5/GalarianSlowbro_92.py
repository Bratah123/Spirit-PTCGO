from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if


def _self_has_special_condition(ctx):
    return bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS))


card = PokemonCardDef(
    guid="a1dd90b4-4dd3-5f22-9eb4-3c7b1646ae0c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowbro.Name",
    display_name="Galarian Slowbro",
    searchable_by=["Galarian Slowbro", "Stage 1", "GalarianSlowbro"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pokémon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, both_actives=True),
        ),
        Attack(
            title="Unhinged Hammer",
            game_text="If this Pokémon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_self_has_special_condition, 120),
        ),
    ],
)
