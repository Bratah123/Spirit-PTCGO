from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import bound_crush, earth_poison, power_gene_passive

card = PokemonCardDef(
    guid="f6ab5174-3bcd-59bb-b6dd-38ce0b917b7a",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Power Gene",
            game_text="As long as Nidoking is in play, your attacks by Nidoran \u2640, Nidorina, Nidoqueen, Nidoran \u2642, and Nidorino do 10 more damage to the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=power_gene_passive(),
        ),
        Attack(
            title="Earth Poison",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=earth_poison(),
        ),
        Attack(
            title="Bound Crush",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 60 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Nidoking can't use Bound Crush during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            locks_next_turn=True,
            effect=bound_crush(),
        ),
    ],
)