from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, bonus_if
from spirit.game.session.effects import is_special_energy


card = PokemonCardDef(
    guid="63b827ee-c7fe-55ad-8ab9-31e346a56d84",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Special Tackle",
            game_text="If this Pok\u00e9mon has any Special Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)), 30),
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)