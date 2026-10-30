from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import psychic_research_own_supporter, flame_jet_snipe

card = PokemonCardDef(
    guid="7cdba2d8-c442-52f8-a22a-fa6dc9e65227",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=['Kirlia', 'Stage 1', 'Kirlia'],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Psychic Research",
            game_text="Search your discard pile for a Supporter card and use the effect of that card as the effect of this attack. (The Supporter card remains in your discard pile.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=psychic_research_own_supporter(),
        ),
        Attack(
            title="Telekinesis",
            game_text="Choose 1 of your opponent's Pokémon. This attack does 40 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=flame_jet_snipe(40),
        ),
    ],
)
