from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="7384f801-e9f5-559f-92f5-2f16b740cb32",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=110,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Primal Fortress",
            game_text="Your Pok\u00e9mon take 30 less damage from attacks from your opponent's Pok\u00e9mon V (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, protects="team",
                                       attacker_pred=lambda p: is_pokemon_v(p.archetype_id)),
        ),
        Attack(
            title="Iron Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=recoil_attack(30),
        ),
    ],
)