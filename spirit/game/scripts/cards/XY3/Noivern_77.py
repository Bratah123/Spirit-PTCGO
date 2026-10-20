from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive
from spirit.game.card_effects.attacks_common import damage_all_opponents




card = PokemonCardDef(
    guid="7a38c5d6-8e2b-503c-9ac9-b1701ef52eb4",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1", "Noivern"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Ability(
            title="Echolocation",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive('Echolocation'),
        ),
        Attack(
            title="Boomburst",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(30),
        ),
    ],
)