from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class _SecretKey(Passive):
    """Each of your Fairy Pokemon's Resistance is now -40."""
    def modify_resistance(self, calc, carrier):
        t = calc.target
        if t is not None and t.owning_player_id == carrier.owning_player_id and \
                PokemonTypes.FAIRY.value in (t.get_attribute(AttrID.POKEMON_TYPES) or []):
            calc.resistance_amount = 40


card = PokemonCardDef(
    guid="66a8f7cd-d636-5c03-a4d3-5fa56f54a569",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Ability(
            title="Secret Key",
            game_text="Each of your Fairy Pok\u00e9mon's Resistance is now -40.",
            passive=_SecretKey(),
        ),
        Attack(
            title="Fairy Lock",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)