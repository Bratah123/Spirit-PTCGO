from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import super_metronome
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="1651d9e5-97c1-59f6-941e-55b7573499e8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Attack(
            title="Super Metronome",
            game_text="Flip a coin. If heads, choose an attack on 1 of your opponent's Pok\u00e9mon. Super Metronome copies that attack except for its Energy cost. (You must still do anything else in order to use that attack.) (No matter what type the Defending Pok\u00e9mon is, Togetic's type is still Colorless.) Togetic performs that attack. (Togetic can make that attack even if it does not have the appropriate number or type of Energy attached to it necessary to make the attack.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=super_metronome,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Togetic; if tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flip_or_nothing(then=protect_next_turn(prevent=True, effects_too=True)),
        ),
    ],
)
