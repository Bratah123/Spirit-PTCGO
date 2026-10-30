from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import electromagnetic_kick
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy

card = PokemonCardDef(
    guid="6b01bbc4-912e-5cee-ad02-69df3059966c",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=['Flaaffy', 'Stage 1', 'Flaaffy'],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Attract Current",
            game_text="Search your deck for a Lightning Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=search_attach_energy(predicate=is_lightning_energy, count=1, distribute=False),
        ),
        Attack(
            title="Electromagnetic Kick",
            game_text="Flip a coin. If tails, Flaaffy does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=electromagnetic_kick(60, 10),
        ),
    ],
)
