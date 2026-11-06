from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon, effective_max_hp
from spirit.game.card_effects.passives_common import boost_own_next_turn


class _HighDensityArmor(Passive):
    """At full HP, opposing attack damage to this Pokemon is reduced by 50 (after W/R)."""
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.target is me):
            return
        if me.get_attribute(AttrID.HP, 0) >= effective_max_hp(calc.board, me):
            calc.amount = max(0, calc.amount - 50)


card = PokemonCardDef(
    guid="5f519eec-9dad-5527-b10a-fd6bc4449c90",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Ability(
            title="High Density Armor",
            game_text="If this Pok\u00e9mon has full HP, any damage done to this Pok\u00e9mon by an opponent's attack is reduced by 50 (after applying Weakness and Resistance).",
            passive=_HighDensityArmor(),
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=boost_own_next_turn(40, attack_title='Overdrive Smash'),
        ),
    ],
)