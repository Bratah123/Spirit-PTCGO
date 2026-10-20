from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _fewer_hp(ctx):
    """This Pokemon has fewer remaining HP than the Defending Pokemon."""
    d = ctx.defender
    return d is not None and ctx.attacker.get_attribute(AttrID.HP, 0) < d.get_attribute(AttrID.HP, 0)


card = PokemonCardDef(
    guid="eeaee165-a025-55e4-ab9c-b6133dd0d3f4",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Emperor's Strike",
            game_text="If this Pok\u00e9mon has fewer remaining HP than the Defending Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_fewer_hp, 60),
        ),
    ],
)