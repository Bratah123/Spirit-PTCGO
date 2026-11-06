from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_chase


card = PokemonCardDef(
    guid="8b54f2e4-2ba9-5651-b7ce-8c26ec2963ce",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownC.Name",
    display_name="Unown [C]",
    searchable_by=["Unown [C]", "Basic", "UnownC"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Chase]",
            game_text="As long as Unown [C] is your Active Pok\u00e9mon, whenever your opponent's Active Pok\u00e9mon tries to retreat, flip a coin. If heads, put 1 damage counter on that Pok\u00e9mon. Apply Weakness and Resistance.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_RETREAT,
            effect=unown_chase,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
