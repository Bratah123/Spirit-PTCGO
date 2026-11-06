from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import psylink_passive


card = PokemonCardDef(
    guid="ebf2e589-dc05-5ad3-a75e-48f04b52685f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAlakazam.Name",
    display_name="Sabrina's Alakazam",
    searchable_by=["Sabrina's Alakazam", "Stage 2", "SabrinasAlakazam"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasKadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psylink",
            game_text="Sabrina's Alakazam always has a copy of every attack your Psychic Pok\u00e9mon in play have (including their Energy costs and anything else required in order to use those attacks, such as discarding Energy cards). This power can't be used if Sabrina's Alakazam is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=psylink_passive,
        ),
        Attack(
            title="Mega Burn",
            game_text="You can't use this attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            locks_next_turn=True,
        ),
    ],
)
