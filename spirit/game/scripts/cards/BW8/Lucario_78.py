from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken


card = PokemonCardDef(
    guid="0c4c6021-054d-5264-8202-8d4cb6872604",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="If this Pok\u00e9mon has any Metal Energy attached to it, this Pok\u00e9mon's type is both Fighting and Metal.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Hurricane Kick",
            game_text="Does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_prizes_taken('opponent'), 30, base=60),
        ),
    ],
)