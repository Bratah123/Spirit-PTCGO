from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import direct_dive

card = PokemonCardDef(
    guid="1a35beb6-44ca-5af8-9158-4487a85afaec",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1", "Prinplup"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Water Drip",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Direct Dive",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            effect=direct_dive,
        ),
    ],
)