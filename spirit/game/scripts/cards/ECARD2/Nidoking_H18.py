from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import earth_rage, earth_rage_condition


card = PokemonCardDef(
    guid="18fede1e-28eb-5344-8bb9-d4853dcab8cf",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=168,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Earth Rage",
            game_text="Once during your turn (before your attack), if Nidoking is your Active Pok\u00e9mon, you may flip a coin. If heads, put a damage counter on each of your opponent's Benched Pok\u00e9mon. This power can't be used if Nidoking is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=earth_rage_condition,
            effect=earth_rage,
        ),
        Attack(
            title="Giant Horn",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
