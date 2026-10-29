from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush
from spirit.game.card_effects.sm5 import total_command

card = PokemonCardDef(
    guid="fc43d57c-6329-53c5-a644-11bc08431812",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Total Command",
            game_text="This attack does 20 damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=total_command,
        ),
        Attack(
            title="Whirlpool",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=rock_crush,
        ),
    ],
)