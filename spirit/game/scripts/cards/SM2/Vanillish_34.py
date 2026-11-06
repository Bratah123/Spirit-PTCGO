from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.attributes import AttrID, PokemonTypes

def _defender_is_fighting(ctx):
    d = ctx.defender
    return d is not None and PokemonTypes.FIGHTING.value in (d.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="2056546d-9964-53c7-bfb3-5a96ebf6a250",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    display_name="Vanillish",
    searchable_by=["Vanillish", "Stage 1", "Vanillish"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_defender_is_fighting, 30),
        ),
    ],
)