from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, damage_per, count_discard
from spirit.game.session.effects import is_pokemon_card


card = PokemonCardDef(
    guid="31474d37-cd9f-57ba-82bb-bae2f077ad52",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Team Plasma", "Flareon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=12,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Vengeance",
            game_text="Does 10 more damage for each Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_discard('mine', is_pokemon_card), 10, base=20),
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=recoil_attack(10),
        ),
    ],
)