from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import condition_on_damaged, flip_tails_discard_energy


card = PokemonCardDef(
    guid="c938d46f-b846-5d3e-be88-6febbf8ac388",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Fire Veil",
            game_text="If Arcanine is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Arcanine is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=condition_on_damaged(SpecialConditions.BURNED),
        ),
        Attack(
            title="Burn Up",
            game_text="Flip a coin. If tails, discard all Fire Energy cards attached to Arcanine.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_tails_discard_energy(PokemonTypes.FIRE, all_energy=True),
        ),
    ],
)
