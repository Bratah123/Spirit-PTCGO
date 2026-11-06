from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import bonus_if


def _fewer_hp_than_defender(ctx):
    defender = ctx.defender
    if defender is None:
        return False
    return ctx.attacker.get_attribute(AttrID.HP, 0) < defender.get_attribute(AttrID.HP, 0)


card = PokemonCardDef(
    guid="4ac62b0e-de77-5585-9fbb-284e2462169d",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Rock Head",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Hammer Kick",
            game_text="If this Pok\u00e9mon has fewer remaining HP than the Defending Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_fewer_hp_than_defender, 30),
        ),
    ],
)