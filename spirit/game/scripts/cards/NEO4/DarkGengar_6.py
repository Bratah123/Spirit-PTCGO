from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import deep_sleep_passive, pull_in


card = PokemonCardDef(
    guid="00fef6d4-4729-5323-b7a7-32579b822862",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGengar.Name",
    display_name="Dark Gengar",
    searchable_by=["Dark Gengar", "Stage 2", "DarkGengar"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHaunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Deep Sleep",
            game_text="As long as any Dark Gengar are in play, a player flips 2 coins for each of his or her Pok\u00e9mon that is Asleep at the end of each turn. If either of them is tails, that Pok\u00e9mon is still Asleep. This power stops working if Dark Gengar is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=deep_sleep_passive,
        ),
        Attack(
            title="Pull In",
            game_text="If your opponent has any Benched Pok\u00e9mon, you may choose 1 of them and switch it with the Defending Pok\u00e9mon (before doing damage or other effects of this attack). Either way, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            effect=pull_in,
        ),
    ],
)
