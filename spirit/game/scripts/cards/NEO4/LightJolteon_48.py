from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import pulse_guard, thunder_needle


card = PokemonCardDef(
    guid="9cd3e873-7642-5e6b-b87c-002d6ba58d66",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightJolteon.Name",
    display_name="Light Jolteon",
    searchable_by=["Light Jolteon", "Stage 1", "LightJolteon"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=135,
    abilities=[
        Attack(
            title="Pulse Guard",
            game_text="During your opponent's next turn, whenever 30 or more damage is done to Light Jolteon (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=pulse_guard,
        ),
        Attack(
            title="Thunder Needle",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads. If you get 2 or more heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=thunder_needle,
        ),
    ],
)
