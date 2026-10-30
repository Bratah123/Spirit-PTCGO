from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ecard import explosive_evolution


card = PokemonCardDef(
    guid="f335917b-8b2f-584f-b5ec-315ef27ee132",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    display_name="Dark Pupitar",
    searchable_by=["Dark Pupitar", "Stage 1", "DarkPupitar"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Rock Tackle",
            game_text="Dark Pupitar does 10 damage to itself. Dark Pupitar can't use this attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            locks_next_turn=True,
            effect=recoil_attack(10),
        ),
        Attack(
            title="Explosive Evolution",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Then, search your deck for an Evolution card named Dark Tyranitar and put it on Dark Pupitar. (This counts as evolving Dark Pupitar.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=explosive_evolution,
        ),
    ],
)
